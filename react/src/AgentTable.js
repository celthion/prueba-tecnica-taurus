// src/AgentTable.js

import React, { useState, useEffect } from 'react';
import { AgGridReact } from 'ag-grid-react';

import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';

function AgentTable() {
  const [rowData, setRowData] = useState([]);

  const columns = [
    { headerName: 'Agent ID', field: 'agent_id', sortable: true, filter: true },
    { headerName: 'Policy Count', field: 'policy_count', sortable: true, filter: true },
    { headerName: 'Total Premium', field: 'total_premium', sortable: true, filter: true },
  ];

  useEffect(() => {
    fetch('http://localhost:8000/groupings/by_agent') 
      .then(result => {
        if (!result.ok) {
          throw new Error('Network response was not ok');
        }
        return result.json();
      })
      .then(data => setRowData(data))
      .catch(error => {
        console.error('Error fetching agent groupings:', error);
      });
  }, []);

  return (
    <div className="ag-theme-alpine" style={{ height: 400, width: '100%' }}>
      <AgGridReact
        rowData={rowData}
        columnDefs={columns}
        pagination={true}
        paginationPageSize={10}
      />
    </div>
  );
}

export default AgentTable;
