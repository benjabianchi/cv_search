import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';

export default function App() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            CVS Search
          </Typography>
          <Button color="inherit">
            Search
          </Button>
          <Button color="inherit">
            Retrain Model
          </Button>
        </Toolbar>
      </AppBar>
    </Box>
  )
}