import * as React from 'react';
import {
  QueryClient,
  QueryClientProvider,
} from "@tanstack/react-query";
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";

import { Box, Container, FormGroup, TextField, Button } from '@mui/material';
import DenseAppBar from './components/DenseAppBar';
import DataTableContainer from './components/DataTableContainer'

const queryClient = new QueryClient();

function App() {
  const [username, setUsername] = React.useState('')
  const [formSubmitted, setFormSubmitted] = React.useState(false)


  const handleFormSubmit = (e) => {
    e.preventDefault()
    setFormSubmitted(true)
  }

  const handleUsernameChange = (e) => {
    e.preventDefault()
    setUsername(e.target.value)
  }

  return (
    <QueryClientProvider client={queryClient}>
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
                <Button variant="contained" onClick={handleFormSubmit} disabled={!username || username === ''}>Grab User</Button>
              </FormGroup>
            </div>
          </Box>
          <DataTableContainer username={username} formSubmitted={formSubmitted} />

        </Container >
      </div >
      <ReactQueryDevtools />
    </QueryClientProvider>
  );
}

export default App;

