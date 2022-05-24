import './App.css';
import Container from '@material-ui/core/Container';

import Routes from "./routes";
import Navbar from "./components/Navbar";

function App() {
  return (
    <div>
      <Navbar />
      <Container maxWidth="sm">
        <Routes />
      </Container>
    </div>
  );
}

export default App;
