import axios from 'axios'

export const API_BASE_URL = 'https://dirty-points-slide-34-168-44-172.loca.lt/theconsole/'

export const getDataByAccountId = async (username) => {
    const { data } = await axios.get(
        `${API_BASE_URL}${username}`
    );
    return data;
}