import { useState } from "react";

import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import IconButton from "@material-ui/core/IconButton";
import ListItemText from "@material-ui/core/ListItemText";
import Delete from "@material-ui/icons/Delete";
import Edit from "@material-ui/icons/Edit";
import Star from "@material-ui/icons/Star";
import SearchBox from "../SearchBox";
import { Icon } from "@material-ui/core";

export default function SearchTechList({ items, onDeleteItem, onUpdateItem }) {
  const [edit, setEdit] = useState({
    id: null,
    value: "",
  });

  const submitUpdate = (value) => {
    onUpdateItem(edit.id, value);
    setEdit({
      id: null,
      value: "",
    });
  };

  if (edit.id) {
    return <SearchBox onAddItem={submitUpdate} edit={edit} />;
  }

  return (
    <List>
      {items.map((item) => {
        return (
          <ListItem key={item.id}>
            <ListItemText  primary={item.tech} />
            <Icon>
              <Star color={item.required ? "action" : "disabled"} />
            </Icon>
            <IconButton edge="end" aria-label="delete">
              <Edit
                onClick={() => setEdit({ id: item.id, value: item.tech })}
              />
            </IconButton>
            <IconButton edge="end" aria-label="delete">
              <Delete onClick={() => onDeleteItem(item.id)} />
            </IconButton>
          </ListItem>
        );
      })}
    </List>
  );
}
