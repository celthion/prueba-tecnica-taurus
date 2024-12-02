// src/TimeSeriesChart.js

import React, { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';

function TimeSeriesChart() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchTimeSeriesData = async () => {
    try {
      const response = await fetch('http://localhost:8000/visualizations/time_series');
      if (!response.ok) {
        throw new Error('Error al obtener los datos de la serie de tiempo');
      }
      const result = await response.json();
      setData(result);
      setLoading(false);
    } catch (error) {
      console.error('Error:', error);
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTimeSeriesData();
  }, []);

  if (loading) {
    return <p>Cargando la visualización...</p>;
  }

  if (!data || data.length === 0) {
    return <p>No hay datos disponibles para la visualización.</p>;
  }

  // Preparar los datos para Plotly
  const dates = data.map(item => item.date);
  const policyCounts = data.map(item => item.policy_count);
  const totalPremiums = data.map(item => item.total_premium);

  const plotData = [
    {
      x: dates,
      y: policyCounts,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Conteo de Pólizas',
      line: { color: '#17BECF' },
    },
    
  ];

  const layout = {
    title: 'Serie de Tiempo de Pólizas',
    xaxis: {
      title: 'Fecha de Creación',
      type: 'date',
      tickformat: '%Y-%m-%d',
    },
    yaxis: {
      title: 'Conteo de Pólizas',
      showgrid: false,
      zeroline: false,
    },
    legend: {
      x: 0,
      y: 1.2,
      orientation: 'h',
    },
    margin: {
      l: 50,
      r: 50,
      t: 80,
      b: 50,
    },
    plot_bgcolor: '#f9f9f9',
    paper_bgcolor: '#f9f9f9',
  };

  return (
    <div>
      <Plot
        data={plotData}
        layout={layout}
        style={{ width: '100%', height: '600px' }}
        config={{ responsive: true }}
      />
    </div>
  );
}

export default TimeSeriesChart;
