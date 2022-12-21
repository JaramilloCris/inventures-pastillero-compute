import ElementList from "./components/ElementList";
import HeaderNavbar from "./components/HeaderNavbar";
import Navbar from "./components/Navbar";

export default function Home() {
  return (
    <div>
      <Navbar />
      <section>
        <HeaderNavbar />
        <div className="separator-container">
          <span className="separator-text">Te queda</span>
        </div>
        <ElementList />
      </section>
    </div>
  );
}
