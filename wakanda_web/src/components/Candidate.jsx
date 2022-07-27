import React from 'react';

const handleClick = () => {
  alert('hello kind ser');
};

const Candidate = ({ name, selected, handleClick }) => {
  return (
    <button
      className={`candidate ${selected ? 'selected' : 'notSelected'}`}
      onClick={() => {
        handleClick();
      }}
    >
      {name}
    </button>
  );
};

export default Candidate;
