import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { NavLink } from "react-router-dom";
import "./index.css";

import {
  faEarthAmericas,
  faTicket,
  faUser,
} from "@fortawesome/free-solid-svg-icons";

const logo = <FontAwesomeIcon icon={faEarthAmericas} />;
const ticket = <FontAwesomeIcon icon={faTicket} />;
const user = <FontAwesomeIcon icon={faUser} />;

const Sidenav = () => {
  return (
    <nav className="sidenav box">
      <div className="logo mb">
        <span>{logo}</span>
        <NavLink to="/">Queue</NavLink>
      </div>
      <ul>
        <li>
          <span>{ticket}</span>
          <NavLink to="/tickets">Tickets</NavLink>
        </li>
        <li>
          <span>{user}</span>
          <NavLink to="/users">Users</NavLink>
        </li>
      </ul>
    </nav>
  );
};

export default Sidenav;
