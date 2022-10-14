import { DataGrid } from "@mui/x-data-grid";
import { useQuery } from "@tanstack/react-query"
import { getDataByAccountId } from '../api'

export default function DataTableContainer({ username, formSubmitted }) {

  const query = useQuery(['userData', username], () => getDataByAccountId(username),
    { enabled: !!username && !!formSubmitted }
  );

  return (
    <DataGrid
      loading={query.isLoading}
      columns={query.data ?? []}
      rows={query.data ?? []}
      pagination
    />
  )
}

