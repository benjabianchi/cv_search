import { useState } from "react";
import SearchBox from "./SearchBox";
import SearchResults from "./SearchResults";

import "./style.css";

export default function AdvancedSearch() {
  const [isAtTop, setIsAtTop] = useState(false);
  const [candidatos, setCandidatos] = useState();

  const handleSearch = async (e) => {
    e.preventDefault();
    setIsAtTop(true);
    const searchText = e.target.elements.techs.value;
    console.log(searchText);
    const request = await fetch("/cvs_index/_search", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: searchText,
    }).catch((err) => console.log(err));
    const response = await request.json();
    setCandidatos(response);
    console.log(candidatos);
  };

  const handleCloseClick = () => {
    setIsAtTop(false);
    setCandidatos(null);
  };

  return (
    <div className="search">
      <SearchBox
        onSearch={handleSearch}
        onClose={handleCloseClick}
        isSearching={isAtTop}
      />
      {candidatos && (
        <SearchResults results={candidatos.hits.hits} isSearching={isAtTop} />
      )}
    </div>
  );
}
