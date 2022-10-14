import axios from "axios";

export const API_BASE_URL =
  "https://5000-indigo-ant-ga6ao2p64oj.ws-us71.gitpod.io/theconsole/";

export const getDataByAccountId = async (username) => {
  try {
    const { data } = await axios.get(`${API_BASE_URL}${username}`);
    return data;
  } catch (e) {
    console.log("error", e.message);
  }
};
