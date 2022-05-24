import { useState } from "react";

import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";
import FormControl from "@material-ui/core/FormControl";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import Checkbox from "@material-ui/core/Checkbox";
import IconButton from "@material-ui/core/IconButton";
import AddCircle from "@material-ui/icons/AddCircle";

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

export default function SearchBox({ onAddItem, onClose, isSearching, edit }) {
  const classes = useStyles();
  const [isRequired, setRequired] = useState(true);
  const [searchText, setSearchText] = useState(edit ? edit.value : "");

  const handleChange = (e) => {
    setRequired(e.target.checked);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onAddItem({
      id: Math.floor(Math.random() * 10000),
      required: isRequired,
      tech: searchText,
    });
    setSearchText("");
  };

  return (
    <form className="search-box-form" onSubmit={handleSubmit}>
      <div className="search-box-input">
        <TextField
          name="techs"
          onChange={({ target: { value } }) => setSearchText(value)}
          value={searchText}
          autoComplete="off"
          type="text"
          label="Tech"
          id="standard-basic"
          color="secondary"
        />
        <FormControl className={classes.formControl}>
          <FormControlLabel
            control={
              <Checkbox
                defaultChecked
                size="small"
                onChange={handleChange}
                value={isRequired}
              />
            }
            label="Obligatorio"
          />
        </FormControl>
        <IconButton
          variant="contained"
          type="submit"
          color="primary"
          className={classes.button}
          disabled={!searchText.length}
        >
          <AddCircle />
        </IconButton>
      </div>
    </form>
  );
}
