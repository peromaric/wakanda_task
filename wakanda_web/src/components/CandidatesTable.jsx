import React from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
} from '@mui/material';

const CandidatesTable = ({ candidates }) => {
  return (
    <TableContainer id="candidatesTable" component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Candidate name</TableCell>
            <TableCell align="right">Candidate age</TableCell>
            <TableCell align="right">Candidate cult</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {candidates.map((candidate) => {
            if (candidate.rank <= 3) {
              return (
                <TableRow
                  key={candidate.name}
                  sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                >
                  <TableCell component="th" scope="row">
                    {candidate.name}
                  </TableCell>
                  <TableCell align="right">{candidate.age}</TableCell>
                  <TableCell align="right">{candidate.cult}</TableCell>
                </TableRow>
              );
            }
          })}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default CandidatesTable;
