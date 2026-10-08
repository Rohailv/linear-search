import streamlit as st

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Linear Search Simulator",
    page_icon="🔎",
    layout="centered"
)

# ---------------------------------------------------------
# Title
# ---------------------------------------------------------
st.title("🔎 Linear Search Simulator")
st.write(
    "Step-by-step visualization of the Linear Search algorithm."
)

st.divider()

# ---------------------------------------------------------
# Input Section
# ---------------------------------------------------------
st.subheader("Enter Input")

array_input = st.text_input(
    "Enter array elements separated by commas",
    placeholder="Example: 10, 25, 7, 42, 18"
)

search_input = st.number_input(
    "Enter element to search",
    value=42,
    step=1
)

# ---------------------------------------------------------
# Initialize Session State
# ---------------------------------------------------------
if "array" not in st.session_state:
    st.session_state.array = []

if "search_value" not in st.session_state:
    st.session_state.search_value = None

if "current_index" not in st.session_state:
    st.session_state.current_index = 0

if "search_started" not in st.session_state:
    st.session_state.search_started = False

if "search_finished" not in st.session_state:
    st.session_state.search_finished = False

if "found_index" not in st.session_state:
    st.session_state.found_index = -1

# ---------------------------------------------------------
# Start Search
# ---------------------------------------------------------
if st.button("▶️ Start Search", use_container_width=True):

    if array_input.strip() == "":
        st.error("Please enter an array.")
    else:

        try:
            array = [
                int(x.strip())
                for x in array_input.split(",")
            ]

            if len(array) == 0:
                st.error("Please enter at least one element.")

            else:
                st.session_state.array = array
                st.session_state.search_value = int(search_input)
                st.session_state.current_index = 0
                st.session_state.search_started = True
                st.session_state.search_finished = False
                st.session_state.found_index = -1

                st.success(
                    "Search started! Click 'Next Step' to begin."
                )

        except ValueError:
            st.error(
                "Invalid input. Please enter numbers separated by commas."
            )

# ---------------------------------------------------------
# Display Array
# ---------------------------------------------------------
if st.session_state.search_started:

    st.subheader("Array")

    array = st.session_state.array
    current_index = st.session_state.current_index
    found_index = st.session_state.found_index

    # Create columns for array elements
    columns = st.columns(len(array))

    for i, value in enumerate(array):

        with columns[i]:

            if i == found_index:

                st.success(
                    f"**{value}**\n\nIndex: {i}"
                )

            elif (
                i == current_index
                and not st.session_state.search_finished
            ):

                st.warning(
                    f"**{value}**\n\nIndex: {i}"
                )

            elif i < current_index:

                st.info(
                    f"**{value}**\n\nIndex: {i}"
                )

            else:

                st.write(
                    f"**{value}**\n\nIndex: {i}"
                )

    st.divider()

    # -----------------------------------------------------
    # Next Step Button
    # -----------------------------------------------------
    if not st.session_state.search_finished:

        if st.button(
            "➡️ Next Step",
            use_container_width=True
        ):

            current = st.session_state.current_index

            # Check if end of array is reached
            if current >= len(array):

                st.session_state.search_finished = True

                st.error(
                    "❌ Element not found. "
                    "The entire array has been checked."
                )

            else:

                current_value = array[current]

                # Check current element
                if current_value == st.session_state.search_value:

                    st.session_state.found_index = current
                    st.session_state.search_finished = True

                    st.success(
                        f"🎉 Element Found!\n\n"
                        f"**{st.session_state.search_value}** "
                        f"was found at index **{current}** "
                        f"(position {current + 1})."
                    )

                else:

                    st.info(
                        f"Comparing **{current_value}** "
                        f"with **{st.session_state.search_value}** "
                        f"→ Not equal.\n\n"
                        f"Moving to the next element."
                    )

                    st.session_state.current_index += 1

                    st.rerun()

    # -----------------------------------------------------
    # Reset Button
    # -----------------------------------------------------
    if st.button(
        "🔄 Reset",
        use_container_width=True
    ):

        st.session_state.array = []
        st.session_state.search_value = None
        st.session_state.current_index = 0
        st.session_state.search_started = False
        st.session_state.search_finished = False
        st.session_state.found_index = -1

        st.rerun()

# ---------------------------------------------------------
# Complexity Section
# ---------------------------------------------------------
st.divider()

st.subheader("📊 Algorithm Complexity")

col1, col2 = st.columns(2)

with col1:
    st.metric("Best Case", "O(1)")
    st.metric("Average Case", "O(n)")

with col2:
    st.metric("Worst Case", "O(n)")
    st.metric("Space Complexity", "O(1)")

# ---------------------------------------------------------
# Algorithm Explanation
# ---------------------------------------------------------
st.divider()

st.subheader("📖 How Linear Search Works")

st.write(
    """
    Linear Search checks each element of an array one by one
    from the beginning until the required element is found.

    **Steps:**

    1. Start from the first element.
    2. Compare the current element with the search value.
    3. If they are equal, the element is found.
    4. If they are not equal, move to the next element.
    5. Continue until the element is found or the entire array is checked.
    """
)

st.subheader("Pseudocode")

st.code(
    """
LINEAR_SEARCH(A, n, key)

for i = 0 to n-1
    if A[i] == key
        return i
    end if
end for

return -1
""",
    language="text"
)