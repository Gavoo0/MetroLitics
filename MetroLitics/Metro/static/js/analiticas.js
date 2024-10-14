Highcharts.chart('container', {
    data: {
        table: 'datatable'
    },
    chart: {
        type: 'column'
    },
    title: {
        text: 'Analiticas Lineas del Metro'
    },
    subtitle: {
        text:
            ''
    },
    xAxis: {
        type: 'category'
    },
    yAxis: {
        allowDecimals: false,
        title: {
            text: 'Cantidad de personas'
        }
    }
});
