import { configureStore } from '@reduxjs/toolkit';
import addressReducer from '../features/address/addressSlice';

export default configureStore({
  reducer: {
    address: addressReducer,
  },
});
