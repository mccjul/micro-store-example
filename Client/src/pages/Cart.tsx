import React from "react";
import { RouteComponentProps } from "@reach/router";
import CartTable from "../components/CartTable";
import { Button } from "@material-ui/core";

const items = [
  { name: "SOMETHING", price: 13.4, amount: 3 },
  { name: "SOMETHING", price: 13.4, amount: 3 },
  { name: "SOMETHING", price: 3.4, amount: 3 },
  { name: "SOMETHING", price: 13.4, amount: 3 }
];
interface Props extends RouteComponentProps {}
export default class Cart extends React.Component<Props> {
  render() {
    return (
      <div>
        <CartTable items={items} />
        <Button style={{ marginTop: 30 }} color="primary" variant="contained">
          Order
        </Button>
      </div>
    );
  }
}
