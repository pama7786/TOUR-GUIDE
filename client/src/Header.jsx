// import "./index.css"
import travelImage from "./travel.jpg";

function Header(){
    return (
        <header>
            <div id='banner'>
            <h1 to="/">Tour Guide</h1>
            <img src={travelImage} alt="Travel" />

            </div>
        </header>
    )
}

export default Header;