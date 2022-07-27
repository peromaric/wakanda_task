import React, { useState } from 'react';
import { useNavigate, useOutletContext } from 'react-router-dom';
import { change } from '../features/address/addressSlice';

const Registration = () => {
  const [address, setAddress] = useOutletContext()[1];
  const navigate = useNavigate();
  const [message, setMessage] = useState('');
  const [positiveMessage, setPositiveMessage] = useState('');
  const [numberOfTokens, setnumberOfTokens] = useOutletContext()[0];

  const addressChange = (e) => {
    setAddress(e.target.value);
    // setRegistered(false);
    // setNrOfTokens(0);
  };

  const setErrorMessage = (e) => {
    setMessage(e);
    setTimeout(() => {
      setMessage('');
    }, 3000);
  };

  const setPositiveMessageWithTimeout = (e) => {
    setPositiveMessage(e);
    setTimeout(() => {
      setPositiveMessage('');
    }, 3000);
  };

  const CheckBalance = async () => {
    try {
      let response = await fetch(
        `http://localhost:8888/balance_of/${address}`,
        {
          method: 'GET',
        }
      );
      let token_number = await response.json();
      
      if (response.status != 200 || token_number < 1) {
        setErrorMessage(data.message);
        return false;
      } else {
        setnumberOfTokens(token_number);
      }
    } catch (message) {
      //console.log(message.message);
      setErrorMessage(message.message);
      return false;
    }
    return true;
  };

  const goToVoting = async () => {
    if (address.trim() != '') {
      let balanceExists = await CheckBalance();
      if (balanceExists) {
        navigate('voting');
      }
    } else {
      setErrorMessage('Please write down address');
    }
  };

  const handleRegister = async () => {
    try {
      let response = await fetch(
        `http://localhost:8888/register_voter/${address}`,
        {
          method: 'GET',
        }
      );
      let status = await response.status;
      if (status == 200) {
        CheckBalance();
        setPositiveMessage('Registration successful');
      } else {
        setErrorMessage(data.message);
      }
    } catch (message) {
      //console.log(message.message);
      setErrorMessage(message.message);
    }
  };

  return (
    <div>
      <h1>Welcome to registration page</h1>
      <p>Enter your address please:</p>
      <input
        type="text"
        value={address}
        onChange={(e) => {
          addressChange(e);
        }}
      ></input>
      <button onClick={handleRegister} id="register">
        Register
      </button>
      <button id="btnGoToVoting" onClick={goToVoting}>
        Go to voting page
      </button>
      <p id="error">{message}</p>
      <p id="positiveMessage">{positiveMessage}</p>
      {/*
       */}

      {/* <h1 id="address">{cornerAddress}</h1>

      <header className="App-header">
        <h1>Hello kind ser please register and vote for a candidate</h1>
        <p>Enter your address please:</p>
        <input
          type="text"
          value={address}
          onChange={(e) => {
            addressChange(e);
          }}
        ></input>
        <button
          onClick={handleRegister}
          id="register"
          className={registered ? 'green' : 'blue'}
        >
          Register
        </button>
        <p>Number of tokens to spend: {nrOfTokens}</p>
        <p>Please select a candidate</p>
        
        <button id="vote" onClick={() => vote()}>
          Vote
        </button>
      </header> */}
    </div>
  );
};

export default Registration;
