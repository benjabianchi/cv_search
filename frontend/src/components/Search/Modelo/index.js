import { useState } from "react";
import SearchBox from "./SearchBox";
import SearchResults from "./SearchResults";

import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContent from "@material-ui/core/DialogContent";
import DialogContentText from "@material-ui/core/DialogContentText";
import DialogTitle from "@material-ui/core/DialogTitle";
import Button from "@material-ui/core/Button";

import "./style.css";

export default function Search() {
  const [isAtTop, setIsAtTop] = useState(false);
  const [candidatos, setCandidatos] = useState();

  const [open, setOpen] = useState(false);

  /* const retrainModel = async e => {
    const request = await fetch('/retrain').catch(err => console.log(err))
    const response = await request.json()
    console.log(response);
  } */

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    setIsAtTop(true);
    const searchTextLowered = e.target.elements.techs.value;
    const request = await fetch("/search", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        key: searchTextLowered,
        limit: e.target.elements.limit.value,
        threshold: e.target.elements.threshold.value,
      }),
    }).catch((err) => console.log(err));
    const response = await request.json();
    setCandidatos(response);
  };

  const handleCloseClick = () => {
    setIsAtTop(false);
    setCandidatos(null);
  };

  return (
    <div className={`search ${isAtTop ? "search--top" : "search--center"}`}>
      <SearchBox
        onSearch={handleSearch}
        onClose={handleCloseClick}
        isSearching={isAtTop}
      />
      {candidatos && (
        <SearchResults results={candidatos.cv} isSearching={isAtTop} />
      )}
      {!candidatos && (
        <div>
          <Button variant="outlined" color="primary" onClick={handleClickOpen}>
            Re-entrenar
          </Button>
          <Dialog
            open={open}
            onClose={handleClose}
            aria-labelledby="alert-dialog-title"
            aria-describedby="alert-dialog-description"
          >
            <DialogTitle id="alert-dialog-title">
              {"Re-entrenar modelo?"}
            </DialogTitle>
            <DialogContent>
              <DialogContentText id="alert-dialog-description">
                Esta acción podría tardar unos minutos. ¿Está seguro que desea
                continuar?
              </DialogContentText>
            </DialogContent>
            <DialogActions>
              <Button onClick={handleClose} color="primary">
                Dale gas
              </Button>
              <Button onClick={handleClose} color="primary" autoFocus>
                Fue
              </Button>
            </DialogActions>
          </Dialog>
        </div>
      )}
    </div>
  );
}
