import { DataGrid } from "@mui/x-data-grid";
import { useQuery } from "@tanstack/react-query";
import { useEffect, useState } from "react";
import { getDataByAccountId } from "../queries/user-data";

const parseColumnHeaders = (data) =>
  Object.keys(data).map((field) => ({ field, key: field }));

export default function DataTableContainer({ username, formSubmitted }) {
  const [columns, setColumns] = useState([]);

  const query = useQuery(
    ["userData", username],
    () => getDataByAccountId(username),
    { enabled: !!username && !!formSubmitted }
  );

  useEffect(() => {
    if (query.data) {
      const tableColumns = parseColumnHeaders(query.data[0]);
      setColumns(tableColumns);
    }
  }, [ query.data]);

  return (
    <div
      style={{ display: "flex", height: "100vh" }}
      className="data-table-container"
    >
      <DataGrid
        loading={query.isLoading}
        columns={columns}
        rows={query.data ?? []}
        pagination
      />
    </div>
  );
}
