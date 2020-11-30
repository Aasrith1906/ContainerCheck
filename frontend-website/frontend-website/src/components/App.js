import { Component } from "react";

class App extends Component
{
  constructor() {
    super();
    this.state = {data:"no data",num_fetches:0};
  }

  getData = async () => {
    const response = await fetch('http://cc-website.api.com/Containers');
    const jsonData = await response.json()
    console.log(jsonData)
    var json = JSON.stringify(jsonData)
    this.setState({data:json})
    this.setState({num_fetches:this.state.num_fetches+1})
  }

  clearData = () =>{

    this.setState({data:"no data"})
  }

  render()
  {
  return (
    <div>
    <button onClick = {this.getData}>fetch container data</button>
    <button onClick = {this.clearData}>clear data</button>
    <br></br>
    <br></br>
      {this.state.data}
    
    <h1>{this.state.num_fetches}</h1>
    </div>
  );
  }

}
export default App;
