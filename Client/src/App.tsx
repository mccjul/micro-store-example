import React, { Component } from "react";
import Header from "./components/Header";
import "./App.css";

import { Router } from "@reach/router";
import Cart from "./pages/Cart";
import Shop from "./pages/Shop";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Header />
        <Router>
          <Cart path="cart" />
          <Shop path="/" />
        </Router>
      </div>
    );
  }
}

export default App;
