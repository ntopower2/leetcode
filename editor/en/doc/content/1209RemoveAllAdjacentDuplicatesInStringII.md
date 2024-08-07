<p>You are given a string <code>s</code> and an integer <code>k</code>, a <code>k</code> <strong>duplicate removal</strong> consists of choosing <code>k</code> adjacent and equal letters from <code>s</code> and removing them, causing the left and the right side of the deleted substring to concatenate together.</p>

<p>We repeatedly make <code>k</code> <strong>duplicate removals</strong> on <code>s</code> until we no longer can.</p>

<p>Return <em>the final string after all such duplicate removals have been made</em>. It is guaranteed that the answer is <strong>unique</strong>.</p>

<p>&nbsp;</p> 
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "abcd", k = 2
<strong>Output:</strong> "abcd"
<strong>Explanation: </strong>There's nothing to delete.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "deeedbbcccbdaa", k = 3
<strong>Output:</strong> "aa"
<strong>Explanation: 
</strong>First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = "pbbcggttciiippooaais", k = 2
<strong>Output:</strong> "ps"
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li> 
 <li><code>2 &lt;= k &lt;= 10<sup>4</sup></code></li> 
 <li><code>s</code> only contains lowercase English letters.</li> 
</ul>

<div><div>Related Topics</div><div><li>String</li><li>Stack</li></div></div><br><div><li>👍 4475</li><li>👎 86</li></div>