// src/App.js

import React from 'react';
import CompanyTable from './CompanyTable';
import AgentTable from './AgentTable';
import StateTable from './StateTable';
import TimeSeriesChart from './TimeSeriesChart';

function App() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Reportes Agrupados</h1>

      <h2>Agrupado por Compañía</h2>
      <CompanyTable />

      <h2>Agrupado por Agente</h2>
      <AgentTable />

      <h2>Agrupado por Estado</h2>
      <StateTable />

      <h2>Visualización de Serie de Tiempo</h2>
      <TimeSeriesChart />
    </div>
  );
}

export default App;
