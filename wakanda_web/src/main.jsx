import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import Registration from './components/Registration';
import Voting from './components/Voting';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from './app/store';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Provider store={store}>
      <Router>
        <Routes>
          <Route path="/" element={<App></App>}>
            <Route index element={<Registration></Registration>}></Route>
            <Route path="voting" element={<Voting></Voting>}></Route>
          </Route>
        </Routes>
      </Router>
    </Provider>
  </React.StrictMode>
);
