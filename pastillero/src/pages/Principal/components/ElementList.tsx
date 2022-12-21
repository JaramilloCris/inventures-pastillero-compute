import { useEffect, useState } from "react";
import Product from "../../../interfaces";

interface ElementListState {
  products: Array<Product>;
}

interface ProductResponse {
  payload: Array<Product>;
}

async function getProducts() {
  const resp = await fetch(
    "https://private-anon-da10b9c8fb-inventurestest.apiary-mock.com/products",
    {
      method: "GET",
      mode: "cors",
      cache: "no-cache",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    }
  );

  const jsonResponse: ProductResponse = await resp.json();
  return jsonResponse;
}

export default function ElementList() {
  const [products, setProducts] = useState<ElementListState["products"]>([]);

  useEffect(() => {
    getProducts().then((products) => {
      setProducts(products.payload);
    });
  }, []);

  return (
    <div>
      {products.map((product: Product, index: number): JSX.Element => {
        const randomNumber: number = Math.floor(Math.random() * 31);
        return (
          <>
            <div key={index} className="list-container">
              <div className="list-container-image">
                <img
                  className="list-image"
                  src={product.imagesUrl}
                  alt={product.name}
                />
              </div>
              <div className="list-container-text">
                <h2 className="list-name">{product.name}</h2>
                <p className="list-concentration">{product.concentration}</p>
                <p
                  className={
                    "list-info " + (randomNumber <= 5 ? "list-info-danger" : "")
                  }
                >
                  Quedan {randomNumber} comprimidos
                </p>
                <p
                  className={
                    "list-info " + (randomNumber <= 5 ? "list-info-danger" : "")
                  }
                >
                  Para {randomNumber} días
                </p>
              </div>
              <div className="list-container-button">
                <button onClick={() => {}} className="list-button" />
              </div>
            </div>
            <div className="stick"></div>
          </>
        );
      })}
    </div>
  );
}
