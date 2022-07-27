import { createSlice } from '@reduxjs/toolkit';

export const addressSlice = createSlice({
  name: 'address',
  initialState: {
    value: '',
  },
  reducers: {
    change: (state, action) => {
      state.value = action.payload;
    },
  },
});

// Action creators are generated for each case reducer function
export const { change } = addressSlice.actions;

export default addressSlice.reducer;
