import { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

import { Outlet, useOutletContext } from 'react-router-dom';

function App() {
  const [address, setAddress] = useState('');
  const [numberOfTokens, setnumberOfTokens] = useState(0);

  return (
    <div className="App">
      <Outlet
        context={[
          [numberOfTokens, setnumberOfTokens],
          [address, setAddress],
        ]}
      ></Outlet>
    </div>
  );
}

export default App;
