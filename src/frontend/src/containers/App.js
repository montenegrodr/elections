import React, { Component } from 'react';
import 'containers/App.css';
import Chart from 'components/Chart'
import { Api } from 'api/api'

class App extends Component {
  constructor(){
      super();
      this.api = new Api();
      this.state = {
          chartData: {}
      }
  }

   async componentDidMount(){
      await fetch('http://localhost:8000/api/aggregate_news/')
          .then(response => response.json())
          .then(parsedJSON => ({
              labels: parsedJSON.labels,
              datasets: Object.keys(parsedJSON.data).map(key => ({
                  label: key,
                  backgroundColor: 'rgb(255, 99, 132)',
                  borderColor: 'rgb(255, 99, 132)',
                  data: parsedJSON.data[key],
                  fill: false,
              })),
          }))
          .then(chartData => this.setState(chartData))
          .catch(error => console.log(error));
      // this.setState({chartData: this.api.getMockData()});
    }

  render() {
    return (
      <div className="App">
        <div>
          <Chart chartData={this.state.chartData}/>
        </div>
      </div>
    );
  }
}

export default App;
