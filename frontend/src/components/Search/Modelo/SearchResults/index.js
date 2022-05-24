import SearchResultsItem from "./SearchResultsItem";

import "./style.css"

export default function SearchResults({ results, isSearching }) {
  console.log(results)
  return (
    <div className="searchResults">
      <table>
        <tbody>
          {!results?.length && isSearching &&
              <tr>
                <td>No hay resultados</td>
              </tr>
          }
          {results?.length >= 1 && isSearching && results?.map((value) => {
            return <SearchResultsItem  key={value[0]} item={value}/>;
          })}
        </tbody>
      </table>
    </div>
  );
}