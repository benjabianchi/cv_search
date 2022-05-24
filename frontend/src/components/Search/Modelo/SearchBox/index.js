import { useState } from "react";

import Button from "@material-ui/core/Button";
import Icon from '@material-ui/core/Icon';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import InputLabel from '@material-ui/core/InputLabel';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';

import "./style.css";

const useStyles = makeStyles((theme) => ({
  button: {
    margin: theme.spacing(1),
  },
  formControl: {
    margin: theme.spacing(1),
    minWidth: 120,
  },
  selectEmpty: {
    marginTop: theme.spacing(2),
  },
}));

export default function SearchBox({ onSearch, onClose, isSearching }) {
  const classes = useStyles();
  const [searchText, setSearchText] = useState("");
  const [limit, setLimit] = useState("");
  const [threshold, setThreshold] = useState("");
  
  const handleCloseClick = () => {
    setSearchText("")
    setLimit("")
    setThreshold("")
    onClose()
  }

  return (
    <div className="search-box">
      <h1 className="search-box-title">Buscardor de candidatos</h1>
      <form className="search-box-form" onSubmit={onSearch}>
        <div className="search-box-input">
          <TextField
            name="techs"
            onChange={({ target: {value}}) => setSearchText(value)}
            value={searchText}
            autoComplete="off"
            type="text"
            label="Techs"
            id="standard-basic"
            color="secondary"
          />
          <FormControl className={classes.formControl}>
            <InputLabel 
              id="select-limit"
              color="secondary"
            >
              Límite
            </InputLabel>
              <Select
                labelId="demo-simple-select-label"
                id="simple-select"
                name="limit"
                value={limit}
                onChange={({ target: {value}}) => setLimit(value)}
                color="secondary"
              >
                <MenuItem value="1">1</MenuItem>
                <MenuItem value="3">3</MenuItem>
                <MenuItem value="5">5</MenuItem>
                <MenuItem value="10">10</MenuItem>
                <MenuItem value="20">20</MenuItem>
                <MenuItem value="30">30</MenuItem>
              </Select>
          </FormControl>
          <FormControl className={classes.formControl}>
            <InputLabel 
              id="select-threshold"
              color="secondary"
            >
                Umbral
            </InputLabel>
            <Select
                labelId="simple-select-label"
                id="simple-select"
                name="threshold"
                value={threshold}
                onChange={({ target: {value}}) => setThreshold(value)}
                color="secondary"
              >
                <MenuItem value="0.7">.5</MenuItem>
                <MenuItem value="0.7">.6</MenuItem>
                <MenuItem value="0.7">.7</MenuItem>
                <MenuItem value="0.8">.8</MenuItem>
                <MenuItem value="0.9">.9</MenuItem>
                <MenuItem value="1">1</MenuItem>
              </Select>
          </FormControl>
        </div>
        
        <div>
          <div>
            <Button
              variant="contained"
              color="primary"
              type="submit"
              className={classes.button}
              disabled={
                !searchText.length ||
                !limit.length ||
                !threshold.length
              }
              endIcon={<Icon>send</Icon>}
            >
              Buscar
            </Button>
            {isSearching &&
            <Button 
              variant="contained"
              color="secondary"
              onClick={handleCloseClick}
            >
              Volver
            </Button>}
          </div>
        </div>
      </form>
    </div>
  );
}