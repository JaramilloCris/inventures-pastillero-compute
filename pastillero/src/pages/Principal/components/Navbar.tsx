export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="left-items">
        <button className="icon-navbar" />
        <span className="text-navbar">Mi pastilero</span>
      </div>
      <div className="right-items">
        <button className="search-navbar" />
        <button className="shop-navbar" />
      </div>
    </nav>
  );
}
