class Api {
    constructor(){
        this.base_uri = 'http://localhost:8000/api/'
    }

    random() {
        return Math.floor(Math.random() * 1000);
    };


    getAggregateNews2(){
        return fetch(this.base_uri + 'aggregate_news/')
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
            .catch(error => console.log(error))
    }

    // getAggregateNews(){
    //    return fetch(this.base_uri + 'aggregate_news/')
    //         .then(
    //             function (response) {
    //                 response.json().then(function (data) {
    //                     return {
    //                         labels: data.labels,
    //                         datasets:  Object.keys(data.data).map(function (key) {
    //                             return {
    //                                 label: key,
    //                                 backgroundColor: 'rgb(255, 99, 132)',
    //                                 borderColor: 'rgb(255, 99, 132)',
    //                                 data: data.data[key],
    //                                 fill: false,
    //                             }
    //                         })
    //                     }
    //                 })
    //             }
    //         ).catch(function (err) {
    //         console.log('Fetch Error :-S', err)
    //     });
    // };

    chartColors = {
        red: 'rgb(255, 99, 132)',
        orange: 'rgb(255, 159, 64)',
        yellow: 'rgb(255, 205, 86)',
        green: 'rgb(75, 192, 192)',
        blue: 'rgb(54, 162, 235)',
        purple: 'rgb(153, 102, 255)',
        grey: 'rgb(201, 203, 207)'
    };

    getMockData() {
        return {
            labels: ['19:10', '19:20', '19:30', '19:40', '19:50', '20:00', '20:10'],
            datasets: [{
                label: 'Jair Bolsonaro',
                backgroundColor: this.chartColors.red,
                borderColor: this.chartColors.red,
                data: [
                    this.random(),
                    this.random(),
                    this.random(),
                    this.random(),
                    this.random(),
                    this.random(),
                    this.random()
                ],
                fill: false,
            }, {
                label: 'Geraldo Alckmin',
                backgroundColor: this.chartColors.blue,
                borderColor: this.chartColors.blue,
                fill: false,
                data: [
                    this.random(),
                    this.random(),
                    this.random(),
                    this.random(),
                    this.random(),
                    this.random(),
                    this.random()
                ],
            }, {
                label: 'Marina Silva',
                backgroundColor: this.chartColors.green,
                borderColor: this.chartColors.green,
                fill: false,
                data: [
                    this.random(),
                    this.random(),
                    this.random(),
                    this.random(),
                    this.random(),
                    this.random(),
                    this.random()
                ],
            }, {
                label: 'Ciro Gomes',
                backgroundColor: this.chartColors.orange,
                borderColor: this.chartColors.orange,
                fill: false,
                data: [
                    this.random(),
                    this.random(),
                    this.random(),
                    this.random(),
                    this.random(),
                    this.random(),
                    this.random()
                ],
            }]
        }
    }
}

module.exports = {Api: Api}