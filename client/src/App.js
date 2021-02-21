
import React from 'react';
const axios = require('axios').default;
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      items: [],
      value: '',
      tu:'3'
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleChange2 = this.handleChange2.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  handleChange(event) {    this.setState({value: event.target.value}); }
  handleChange2(event) {    this.setState({tu: event.target.tu}); }
  handleSubmit(event) {
    console.log(this.state.value,this.state.tu)
    if (!this.state.value){
      this.props.onChange(null)
    }
    //console.log(typeof Number(this.state.value))
    event.preventDefault();
    var url='http://185.244.172.149:8080/'+Number(this.state.value)+'/'+Number(this.state.tu)

    axios.get(url).then((response) => {
      console.log(response['data'])
  this.setState({
    isLoaded: true,
    items:[response['data']]
  });
}, (error) => {
  console.log(error);
});

event.preventDefault();
}


render() {
  const { error, isLoaded, items } = this.state;
  if (error) {
    return (
    <form onSubmit={this.handleSubmit} name="frm"> <label>
    Ccal:
    <input type="number"  value={this.state.value} onChange={this.handleChange} onclick="return IsEmpty();"/>        </label>
    <input type="submit" value="Submit" />
    </form>);
    //<div>Ошибка: {error.message}</div>;
  }  else {
    return (
      <div>
      <form onSubmit={this.handleSubmit} name="frm"> <label>
      </label>
      <center>Points:<input type="number" value={this.state.value} onChange={this.handleChange} onclick="return IsEmpty();"/></center>
      <center><input type="submit" value="Submit" /></center>
      </form>
      {items.map(item => (
        <div>
        <center>
            <p>Name:{item.name}     &nbsp;      Nationality:{item.nationality}</p>
            <p>Power:{item.power}     &nbsp; &nbsp; &nbsp;  Will:{item.will}</p>
            <p>Agility:{item.agility}   &nbsp;   &nbsp;&nbsp; Health:{item.health}</p>
            <p>Intellgence:{item.intellgence}   &nbsp;&nbsp;   &nbsp;         HP:{item.hp}</p>
            <p> &nbsp; Perception:{item.perception}</p>
            <p>Forward dmg:{item.prm}   &nbsp;&nbsp;   &nbsp;         Aplitude dmg:{item.amp}</p>
            <p> &nbsp; Weapon:{item.weapon[0]}&nbsp;{item.weapon[1]}</p>
            <p>Base Speed:{item.base_speed}   &nbsp;    Base Action:{item.base_action}</p>
          </center>
          </div>
          ))}
      </div>
   );
  }
}
}

export default MyComponent;
