import React from 'react';
import { useOutletContext } from 'react-router-dom';
import { useState, useEffect } from 'react';
import Candidate from '../components/Candidate';
import CandidatesTable from './CandidatesTable';

const Voting = () => {
  const [numberOfTokens, setnumberOfTokens] = useOutletContext()[0];
  const [address, setAddress] = useOutletContext()[1];
  const [candidates, setCandidates] = useState([]);
  const [message, setMessage] = useState('');
  const [typeOfMessage, setTypeOfMessage] = useState('');
  const [messageCount, setMessageCount] = useState(0);

  let messageBlock = <h1 id={typeOfMessage}>{message}</h1>;

  const canSelect = (c) => {
    if (c.selected == true) {
      return true;
    }

    let numberOfSelected = 0;
    candidates.forEach((can) => {
      numberOfSelected += can.selected ? 1 : 0;
    });
    return numberOfSelected < numberOfTokens;
  };

  const handleClick = (c) => {
    if (!canSelect(c)) {
      setErrorMessage(
        'You can not select more candidates than your current balance'
      );
      return;
    }

    c.selected = !c.selected;
    setCandidates(candidates.map((c) => c));
  };

  const getSelectedCandidates = () => {
    let selectedCandidates = [];
    candidates.forEach((c) => {
      if (c.selected) {
        selectedCandidates.push(c);
      }
    });
    return selectedCandidates;
  };

  // const ClearMessageIfQueueEmpty = (mc) => {
  //   let messageCountLocal = mc;
  //   setMessageCount(messageCountLocal - 1);
  //   console.log(messageCountLocal);
  //   if (messageCountLocal - 1 < 1) {
  //     setMessage('');
  //   }
  // };

  const setMessageText = (e, typeOfMessage) => {
    setMessage(e);
    setTypeOfMessage(typeOfMessage);
    setTimeout(() => {
      setMessage('');
    }, 3000);
  };

  useEffect;

  const setPositiveMessage = (e) => {
    setMessageText(e, 'positiveMessage');
  };

  const setErrorMessage = (e) => {
    setMessageText(e, 'error');
  };

  const vote = async () => {
    if (numberOfTokens < 1) {
      setErrorMessage("You don't have enough tokens to vote");
      return;
    }

    const selectedCandidates = getSelectedCandidates();
    selectedCandidates.forEach(async (c) => {
      let response = await fetch(
        `http://localhost:8888/candidate_list/`,
        {
          method: 'GET',
        }
      );
      let data = await response.json();
      if (data.code == 100) {
        setnumberOfTokens(data.numberOfTokens);
        setCandidates(
          candidates.map((c) => {
            c.selected = false;
            return c;
          })
        );
        setPositiveMessage('Vote successful');
      }
    });
  };

  useEffect(() => {
    fetch('http://localhost:8888/candidate_list/')
      .then((res) => res.json())
      .then((res) => {
        setCandidates(res.candidates);
      });
  }, []);

  return (
    <div>
      <h1>Welcome to voting page</h1>
      <p>Thank you for registering with address: {address}</p>
      <p id="numberOfTokens">Number of tokens to spend: {numberOfTokens}</p>
      <p>List of candidates:</p>
      <div className="candidates">
        {candidates.map((c, ix) => {
          return (
            <Candidate
              name={c.name}
              selected={c.selected}
              key={ix}
              handleClick={() => {
                handleClick(c);
              }}
            ></Candidate>
          );
        })}
      </div>
      <p>Select at least one candidate and press Vote</p>
      <h2>Top 3 candidates</h2>
      <CandidatesTable candidates={candidates}></CandidatesTable>
      <button className="button vote" onClick={vote}>
        Vote
      </button>
      {messageBlock}
    </div>
  );
};

export default Voting;
