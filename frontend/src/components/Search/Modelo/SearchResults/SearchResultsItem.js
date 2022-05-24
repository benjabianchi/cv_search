import "./style.css"
import GetAppIcon from '@material-ui/icons/GetApp';
import IconButton from '@material-ui/core/IconButton';

export default function SearchResultsItem({ item }) {
  console.log(item);
  return (
    <tr>
      <td>{item[0]}</td>
      <td>{item[1]}</td>
      <td>
        <IconButton color="primary" aria-label="upload picture" component="span">
          <GetAppIcon />
        </IconButton>
      </td>
    </tr>
  );
}