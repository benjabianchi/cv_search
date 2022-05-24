import "./style.css";
import GetAppIcon from "@material-ui/icons/GetApp";
import IconButton from "@material-ui/core/IconButton";

export default function SearchResultsItem({ item }) {
  return (
    <tr>
      <td>{item}</td>
      <td>
        <IconButton
          color="primary"
          aria-label="upload picture"
          component="span"
        >
          <GetAppIcon />
        </IconButton>
      </td>
    </tr>
  );
}
