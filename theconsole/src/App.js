import * as React from 'react';
import { Box, Container, FormGroup, TextField, Button, Paper, Grid, FormLabel } from '@mui/material';
import { useEffect } from 'react';
import { grabUser } from './api';
import DenseAppBar from './components/DenseAppBar';
import { DataGrid } from '@mui/x-data-grid';



function App() {
  const [username, setUsername] = React.useState('')
  const [tableRows, setTableRows] = React.useState([])
  const [tableCols, setTableCols] = React.useState([])

  useEffect(() => {
    console.log(tableRows);
    console.log(tableCols)
  }, [tableRows, tableCols])

  const fetchData = async () => {
    const data = await grabUser(username);
    const columnDefs = Object.keys(data[0]).map(field => ({ field, width: 130 }));
    setTableCols(columnDefs)
    setTableRows(data)
  }

  const handleUsernameChange = (e) => {
    e.preventDefault()
    setUsername(e.target.value)
  }

  return (
    <div className="App">
      <DenseAppBar />
      <Container maxWidth="xl" style={{ paddingTop: 20 }}>
        <Box
          component="form"
          noValidate
          autoComplete="off"
        >
          <div>
            <FormGroup row={true}>
              <TextField name="username" label="Username" variant="outlined" required onChange={handleUsernameChange} value={username} />
              <Button variant="contained" onClick={fetchData} disabled={!username || username === ''}>Grab User</Button>
            </FormGroup>
          </div>
        </Box>
        <div style={{ display: 'flex', height: 800 }}>
          <div style={{ flexGrow: 1 }}>
            <DataGrid
              columns={tableCols}
              rows={tableRows}
            />
          </div>
        </div>
      </Container >
    </div >
  );
}

export default App;

