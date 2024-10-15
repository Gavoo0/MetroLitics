Highcharts.chart('container', {
    data: {
        table: 'datatable'
    },
    chart: {
        type: 'column'
    },
    title: {
        text: 'Aglomeración por Línea de Metro'
    },
    yAxis: {
        allowDecimals: false,
        title: {
            text: 'Cantidad de Aglomeración'
        }
    },
    xAxis: {
        title: {
            text: 'Líneas de Metro'
        }
    },
    series: [{
        name: 'Aglomeración (Ayer)',
        dataLabels: {
            enabled: false
        },
        pointWidth: 50  // Ajusta el ancho de las barras aquí
    }, {
        name: 'Aglomeración (Hoy)',
        dataLabels: {
            enabled: false
        },
        pointWidth: 50  // Ajusta el ancho de las barras aquí
    }]
});
