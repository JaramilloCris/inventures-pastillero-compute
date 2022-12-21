import pastilla from "../../.././assets/images/pastilla.png";

export default function HeaderNavbar() {
  return (
    <div className="container">
      <div className="header-element">
        <img className="header-image" src={pastilla} alt={"pastilla"} />
      </div>
      <div className="header-element">
        <h1 className="header-text">Revisa tus compras</h1>
      </div>
      <div className="header-element">
        <p className="header-text header-subtitle">
          Agrega al carro si necesitas reponer
        </p>
      </div>
    </div>
  );
}
