import { Component } from "react";
import AppBar from '@material-ui/core/AppBar'
import Toolbar from '@material-ui/core/Toolbar'
import Typography from '@material-ui/core/Typography'
import ContainerItem from "./ContainerDisplay"
import { ListItem } from '@material-ui/core';
import { List } from '@material-ui/core';
import { ListItemText } from '@material-ui/core';
import { Button } from '@material-ui/core';
import ContainerForm from "./ContainerForm";

class App extends Component
{
  constructor() {
    super();
    this.state = {data:"",num_fetches:0,formdata:""};
    this.getData();
  }

  getData = async () => {

    try {
      const response = await fetch('http://cc-website.api.com/Containers');
      const jsonData = await response.json()
      console.log(jsonData)
      this.setState({data:jsonData["data"]})
      this.setState({num_fetches:this.state.num_fetches+1})
      
    } catch (error) {
      this.setState({data:error})
    }
    
  }

  formCallback = (form_data) => {
    this.setState({formdata:form_data});
  } 

  clearData = () =>{

    this.setState({data:""})
  }

  render()
  {
  return (
    <div>
      <Button onClick={this.getData} variant="outlined" color="primary">Click to get data</Button>
      <Button onClick={this.clearData } variant="outlined" color="primary">Click to clear </Button>
      <List>
        {
          Object.keys(this.state.data).map((key,index) => (
            <ContainerItem name={key} data={JSON.stringify(this.state.data[key])}/>
          ))
        } 
   
      </List>

      <ContainerForm parentCallback={this.formCallback}/>
      <h1>{this.state.formdata}</h1>
    </div>
  );
  }

}
export default App;
