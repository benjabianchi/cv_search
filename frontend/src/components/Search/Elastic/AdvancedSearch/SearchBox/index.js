import { useState } from "react";

import Button from "@material-ui/core/Button";
import Icon from "@material-ui/core/Icon";
import IconButton from "@material-ui/core/IconButton";
import HelpIcon from "@material-ui/icons/Help";
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";
import ClickAwayListener from "@material-ui/core/ClickAwayListener";
import Box from "@material-ui/core/Box";

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

const listenerStyles = {
  position: "absolute",
  top: 28,
  right: 0,
  left: 0,
  zIndex: 1,
  border: "1px solid",
  p: 1,
  bgcolor: "background.paper",
};

export default function SearchBox({ onSearch, onClose, isSearching }) {
  const classes = useStyles();
  const [searchText, setSearchText] = useState("");
  const [listenerOpen, setListenerOpen] = useState(false);

  const handleCloseClick = () => {
    setSearchText("");
    onClose();
  };

  const handleListenerClick = () => {
    setListenerOpen((prev) => !prev);
  };

  const handleListenerClickAway = () => {
    setListenerOpen(false);
  };

  return (
    <div className="search-box">
      <form className="search-box-form" onSubmit={onSearch}>
        <div className="search-box-input">
          <TextField
            name="techs"
            onChange={({ target: { value } }) => setSearchText(value)}
            value={searchText}
            autoComplete="off"
            type="text"
            label="Techs"
            id="standard-multiline-static"
            multiline
            color="secondary"
          />
        </div>

        <div>
          <div>
            <Button
              variant="contained"
              color="primary"
              type="submit"
              className={classes.button}
              disabled={!searchText.length}
              endIcon={<Icon>send</Icon>}
            >
              Buscar
            </Button>
            {isSearching && (
              <Button
                variant="contained"
                color="secondary"
                onClick={handleCloseClick}
              >
                Volver
              </Button>
            )}
          </div>
          <ClickAwayListener onClickAway={handleListenerClickAway}>
            <Box sx={{ position: "relative" }}>
              <IconButton type="button" onClick={handleListenerClick}>
                <HelpIcon />
              </IconButton>
              {listenerOpen ? (
                <Box sx={listenerStyles}>
                  {`{
                    "query": {
                      "bool": {
                        "must": [
                          {
                            "match": {
                              "words": "python java"
                            }
                          }
                        ],
                      "should": [
                        {
                          "match": {
                            "local": "Buenos Aires"
                          }
                        }
                      ]
                      }
                    }
                  }`}
                </Box>
              ) : null}
            </Box>
          </ClickAwayListener>
        </div>
      </form>
    </div>
  );
}
