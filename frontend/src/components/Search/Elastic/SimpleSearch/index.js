import { useState } from "react";
import SearchBox from "./SearchBox";
import SearchResults from "./SearchResults";
import SearchTechList from "./SearchTechList";

import Box from "@material-ui/core/Box";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";

import "./style.css";

export default function SimpleSearch() {
  const [isAtTop, setIsAtTop] = useState(false);
  const [candidatos, setCandidatos] = useState();
  const [items, setItems] = useState([]);

  function makeBody() {
    const mustTechs = items
      .filter(item => item.required)
      .map(item => {return item.tech})
      .join(" ");
    const shouldTechs = items
      .filter(item => !item.required)
      .map(item => {return item.tech})
      .join(" ");
    console.log(mustTechs, " -- ",shouldTechs);
    return({
      query: {bool: {
        must: [{match: {words: mustTechs}}],
        should: [{match: {words: shouldTechs}}]
      }}
    })
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    setIsAtTop(true);
    const query = makeBody();
    const request = await fetch("/cvs_index/_search", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(query)
    }).catch((err) => console.log(err));
    const response = await request.json();
    setCandidatos(response);
    console.log(response);
  };

  const handleCloseClick = () => {
    setIsAtTop(false);
    setCandidatos(null);
  };

  const handleAddItem = (item) => {
    const newItem = [...items, item]
    setItems(newItem)
    console.log(items)
  };

  const updateTech = (itemId, newValue) => {
    setItems((prev) =>
      prev.map((item) => (item.id === itemId ? newValue : item))
    );
  };

  const deleteTech = (id) => {
    const removeArr = [...items.filter((item) => item.id !== id)];
    setItems(removeArr);
  };

  return (
    <div className="search">
      <SearchBox
        onAddItem={handleAddItem}
        onClose={handleCloseClick}
        isSearching={isAtTop}
      />
      <Typography sx={{ mt: 4, mb: 2 }} variant="h6" component="div">
        Techs requeridas para candidatos
      </Typography>
      <Box sx={{ flexGrow: 1, maxWidth: 752, width: 300 }}>
        {items && (
          <SearchTechList
            items={items}
            onDeleteItem={deleteTech}
            onUpdateItem={updateTech}
          />
        )}
      </Box>
      <Button 
        variant="contained"
        color="primary"
        type="submit"
        onClick={handleSearch}
      >
        Buscar
      </Button>
      {candidatos && (
        <SearchResults results={candidatos.hits.hits} isSearching={isAtTop} />
      )}
    </div>
  );
}
