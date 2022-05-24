import { BrowserRouter as Router, Link, Route, Switch } from "react-router-dom";
import Search from "../components/Search/Modelo";
import Login from "../components/Login";
import Retrain from "../components/Retrain";
import Elastic from "../components/Search/Elastic";

export default function Routes() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact>
          <Login />
        </Route>
        <Route path="/search/modelo" exact>
          <Search />
        </Route>
        <Route path="/search/elastic" exact>
          <Elastic />
        </Route>
        <Route path="/retrain" exact>
          <Retrain />
        </Route>
      </Switch>
    </Router>
  );
}