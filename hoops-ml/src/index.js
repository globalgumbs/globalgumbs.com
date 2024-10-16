import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

import { Amplify } from 'aws-amplify'
import config from './aws-exports'
import { get } from 'aws-amplify/api'


Amplify.configure(config)

async function getData() {
  try {
    const request = get({
      apiName: 'HoopAPI', 
      path: '/'
    })
    const response = await request.response;
    console.log(response)
  } catch (e) {
    console.log('GET call failed: ', JSON.parse(e.response.body))
  }
};


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

export { getData };
