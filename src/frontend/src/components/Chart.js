import React, { Component } from 'react';
import { Line } from 'react-chartjs-2'

class Chart extends Component{
    constructor(props){
        super(props);
        this.state = {
            chartData: props.chartData
        }
    }

    render(){
        return(
            <div className="chart">
                <Line
                    data={this.state.chartData}
                    options={{
                        title:{
                            display:true,
                            text:'Volume de noticias',
                            fontSize: 25
                        },
                        legend:{
                            display:true,
                            position:'right'
                        }
                    }}
                />
            </div>
        )
    }
}

export default Chart;