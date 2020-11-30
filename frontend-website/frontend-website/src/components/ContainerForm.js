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


export default class ContainerForm extends Component
{
    constructor(props)
    {
        super(props)
        this.setState({cname:"",containerdata : ""})
    }

    setCname = (Cname)=>{
        this.setState({cname:Cname})
    }

    getContainerInfo = async () => {

        try {

            const url = "http://cc-website.api.com/Containers/";
            const url_for_container = url.concat(this.state.cname);
            const response = await fetch(url_for_container);
            const jsonData = await response.json()
            this.setState({containerdata:JSON.stringify(jsonData["data"])})
          } catch (error) {
            this.setState({containerdata:error})
          }

    }

    form_submit = (event)=>{
        event.preventDefault()
        this.getContainerInfo()
        this.props.parentCallback(this.state.containerdata)
    }

    render()
    {
        return (
        <div
            style={{
            display: "flex",
            justifyContent: "center",
            margin: 20,
            padding: 20
            }}
        >
        <form style={{ width: "50%" }} onSubmit={this.form_submit}>
          <h1>Get Individual Container</h1>

          <FormControl margin="normal" fullWidth>
            <InputLabel htmlFor="name">Container Name</InputLabel>
            <Input id="name" type="text" onInput={e=>this.setCname(e.target.value)}/>
          </FormControl>

          <Button type="submit" variant="contained" color="primary" size="medium">
            Send
          </Button>
        </form>
      </div>
        );
    }
}

