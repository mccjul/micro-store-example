import React from "react";
import { RouteComponentProps } from "@reach/router";
import ShopItems from "../components/ShopItems";

const items = [
  { name: "SOMETHING", price: 13.4, amount: 3 },
  { name: "SOMETHING", price: 13.4, amount: 3 },
  { name: "SOMETHING", price: 3.4, amount: 3 },
  { name: "SOMETHING", price: 13.4, amount: 3 }
];
interface Props extends RouteComponentProps {}
export default class Shop extends React.Component<Props> {
  render() {
    return (
      <div style={{ flex: 1, flexDirection: "row" }}>
        {items.map(item => (
          <ShopItems name={item.name} price={item.price} amount={item.amount} />
        ))}
      </div>
    );
  }
}
