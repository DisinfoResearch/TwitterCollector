import axios from 'axios'

const API_BASE_URL = 'https://dirty-otters-lead-34-82-185-238.loca.lt/theconsole/'

export async function grabUser (username = '') {
    const response = await axios.get(`${API_BASE_URL}${username}`)
    const json = response.data;
    console.log(json)
    return json
}