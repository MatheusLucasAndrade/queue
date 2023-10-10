from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
import pytest
from app.services.users import UserService


class TestUserService:
    def test_get_all_user_returns_list_of_users(self, mocker):
        user_service = UserService("fake_db", "fake_collection")

        mocker.patch.object(
            user_service.collection,
            "find",
            return_value=[{"user_name": "Fake Name"}, {"user_name": "Fake Name II"}],
        )

        result = user_service.get_all_user()

        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0]["user_name"] == "Fake Name"
        assert result[1]["user_name"] == "Fake Name II"

    def test_raises_http_exception_when_no_users_exist(self, mocker):
        user_service = UserService("fake_db", "fake_collection")

        mocker.patch.object(user_service.collection, "find", return_value=[])

        with pytest.raises(HTTPException) as e:
            user_service.get_all_user()
        assert e.value.status_code == 404

    def test_returns_list_of_users_matching_contains_string(self, mocker):
        user_service = UserService("fake_db", "fake_collection")

        contains = "John"
        expected_result = [
            {"user_name": "John Doe", "user_profile": "ADMIN"},
            {"user_name": "John Smith", "user_profile": "MODERADOR"},
        ]

        mocker.patch.object(user_service, "collection")
        user_service.collection.find.return_value = expected_result

        result = user_service.get_by(contains)

        assert result == expected_result
        assert len(result) == 2

    def test_should_not_return_data_on_list_of_datas(self, mocker):
        user_service = UserService("fake_db", "fake_collection")

        mocker.patch.object(user_service.collection, "users")

        with pytest.raises(HTTPException) as e:
            user_service.get_by("None")

        assert e.value.status_code == 404
