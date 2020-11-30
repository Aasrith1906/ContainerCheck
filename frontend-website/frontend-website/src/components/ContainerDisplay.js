import { Component } from "react";
import AppBar from '@material-ui/core/AppBar'
import Toolbar from '@material-ui/core/Toolbar'
import Typography from '@material-ui/core/Typography'
import { Container } from "@material-ui/core";
import { ListItem } from '@material-ui/core';
import { ListItemText } from '@material-ui/core';
import {
    FormControl,
    InputLabel,
    Input,
    Button,
    TextField
  } from "@material-ui/core";

export default class ContainerItem extends Component 
{
    constructor(props)
    {
        super(props)
        this.state = {name:this.props.name , data:this.props.data}
    }

    render()
    {
        return (
        <div>
            <ListItem button component="a">
            <ListItemText primary={this.state.name}/>
            <ListItemText primary= {this.state.data}/>
            </ListItem>
        </div>
        );
    }

}

